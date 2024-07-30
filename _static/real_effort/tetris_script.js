// Select the canvas and h2 elements
let canvas = document.querySelector("#tetris");
let scoreboard = document.getElementById("scoreboard");
let nextBlockCanvas = document.querySelector("#next-block");

// Get the 2D rendering context for the canvas
let ctx = canvas.getContext("2d");

// Scale up the size of the context to make the blocks bigger
ctx.scale(30,30);

// Get the 2D rendering context for the next block canvas
let nextBlockCtx = nextBlockCanvas.getContext("2d");

// Scale up the size of the next block context to make the blocks bigger
nextBlockCtx.scale(20, 20);

// Array of different shapes the blocks can be
const SHAPES = [
    [
        [0,1,0,0], // shape 1
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ],
    [
        [0,1,0],  // shape 2
        [0,1,0],
        [1,1,0]
    ],
    [
        [0,1,0],  // shape 3
        [0,1,0],
        [0,1,1]
    ],
    [
        [1,1,0],  // shape 4
        [0,1,1],
        [0,0,0]
    ],
    [
        [0,1,1],  // shape 5
        [1,1,0],
        [0,0,0]
    ],
    [
        [1,1,1],  // shape 6
        [0,1,0],
        [0,0,0]
    ],
    [
        [1,1],    // shape 7
        [1,1],
    ]
]

// Array of colors for each shape
const COLORS = [
    "#fff",    // color for shape 1
    "#9b5fe0", // color for shape 2
    "#16a4d8", // color for shape 3
    "#60dbe8", // color for shape 4
    "#8bd346", // color for shape 5
    "#efdf48", // color for shape 6
    "#f9a52c", // color for shape 7
    "#d64e12"  // color for shape 8
]

// The number of rows in the grid
const ROWS = 20;

// The number of columns in the grid
const COLS = 10;

// The number of rows to be finished per task
const ROWS_PER_TASK = 2;

// The speed of falling block (interval in ms)
const SPEED = 310;

// Allowing the user to speed up the falling block by pressing the down arrow key
const ALLOW_DOWN_KEY = false;

// Generate the empty grid for the game
let grid = generateGrid();

// The falling block object
let fallingPieceObj = null;

// The score of the game
let score = 0;

// The flag to indicate if the game is over (task completed)
let gameOver = false;

// Set interval to update the game state every 0.5s
setInterval(newGameState,SPEED);

// Function to update the game state
function newGameState() {
    checkGrid();
    if (score >= ROWS_PER_TASK) {
        // If the score exceeds or meets ROWS_PER_TASK, stop the game and display "Game Over" message
        scoreboard.innerHTML = "Task Completed";
        gameOver = true;
        document.getElementById("continue-btn").style.display = "block";
        clearInterval(gameInterval);
        return;
    }
    if (!fallingPieceObj) {
        // If there is no falling block, generate a new one
        fallingPieceObj = randomPieceObject();
        renderPiece();
    }
    moveDown();
    renderNextBlock();
}
// function to check if a full row exists and if so, removes the row and increments the score
function checkGrid(){
    let count = 0;
    // loop through the rows of the grid
    for(let i=0;i<grid.length;i++){
        let allFilled = true;
        // loop through the columns of the current row
        for(let j=0;j<grid[0].length;j++){
            // if there is an empty space in the current row, set allFilled to false
            if(grid[i][j] == 0){
                allFilled = false
            }
        }
        // if all spaces in the current row are filled, increment the count and remove the row
        if(allFilled){
            count++;
            grid.splice(i,1);
            grid.unshift([0,0,0,0,0,0,0,0,0,0]);
        }
    }
    // update the score based on the number of rows removed
    if(count == 1){
        score+=1;
    }else if(count == 2){
        score+=2;
    }else if(count == 3){
        score+=3;
    }else if(count>3){
        score+=4
    }
    // update the score display
    scoreboard.innerHTML = "Rows Completed: " + score;
}

// function to generate an empty grid with specified number of rows and columns
function generateGrid(){
    let grid = [];
    for(let i=0;i<ROWS;i++){
        grid.push([]);
        for(let j=0;j<COLS;j++){
            grid[i].push(0)
        }
    }
    return grid;
}

// function to generate a random falling piece object
// modified to include a nextPieceObj to store the next piece
let nextPieceObj = randomPiece();

function randomPieceObject() {
    if (!nextPieceObj) {
        nextPieceObj = randomPiece();
    }
    let currentPiece = nextPieceObj;
    nextPieceObj = randomPiece();

    let x = 4;
    let y = 0;
    return { ...currentPiece, x, y };
}

function randomPiece() {
    let ran = Math.floor(Math.random() * 7);
    let piece = SHAPES[ran];
    let colorIndex = ran + 1;
    return { piece, colorIndex };
}


// function to render the falling piece
function renderPiece(){
    let piece = fallingPieceObj.piece;
    for(let i=0;i<piece.length;i++){
        for(let j=0;j<piece[i].length;j++){
            if(piece[i][j] == 1){
            ctx.fillStyle = COLORS[fallingPieceObj.colorIndex];
            ctx.fillRect(fallingPieceObj.x+j,fallingPieceObj.y+i,1,1);
        }
        }
    }
}

// function to render the next piece
//also keep the background transparent, only set the color of the block
// clear the canvas when new piece is generated
function renderNextBlock() {
    nextBlockCtx.clearRect(0, 0, 4, 4);
    let piece = nextPieceObj.piece;
    for (let i = 0; i < piece.length; i++) {
        for (let j = 0; j < piece[i].length; j++) {
            if (piece[i][j] == 1) {
                nextBlockCtx.fillStyle = COLORS[nextPieceObj.colorIndex];
                nextBlockCtx.fillRect(j, i, 1, 1);
            }
        }
    }
}

// function to move the falling piece down
//Move the falling piece downwards by checking if there's no collision
function moveDown(){
    //Check if there's no collision when moving the piece downwards
    if(!collision(fallingPieceObj.x, fallingPieceObj.y + 1)){
        //If there's no collision, move the piece downwards
        fallingPieceObj.y += 1;
    } else {
        //If there's a collision, stop the piece from moving
        let piece = fallingPieceObj.piece;

        //Loop through the piece to place it on the grid
        for(let i = 0; i < piece.length; i++){
            for(let j = 0; j < piece[i].length; j++){
                if(piece[i][j] == 1){
                    //Calculate the grid position of the piece
                    let p = fallingPieceObj.x + j;
                    let q = fallingPieceObj.y + i;
                    //Place the piece on the grid
                    grid[q][p] = fallingPieceObj.colorIndex;
                }
            }
        }

        //Check if the piece has reached the top of the grid
        if(fallingPieceObj.y == 0){
            //Reset the grid and keep the score
            grid = generateGrid();
        }

        //Set falling piece to null
        fallingPieceObj = null;
    }

    //Render the game
    renderGame();
}

//Move the falling piece leftwards by checking if there's no collision
function moveLeft(){
    //Check if there's no collision when moving the piece leftwards
    if(!collision(fallingPieceObj.x - 1, fallingPieceObj.y)){
        //If there's no collision, move the piece leftwards
        fallingPieceObj.x -= 1;
    }

    //Render the game
    renderGame();
}

//Move the falling piece rightwards by checking if there's no collision
function moveRight(){
    //Check if there's no collision when moving the piece rightwards
    if(!collision(fallingPieceObj.x + 1, fallingPieceObj.y)){
        //If there's no collision, move the piece rightwards
        fallingPieceObj.x += 1;
    }

    //Render the game
    renderGame();
}

//Rotate the falling piece by 90 degrees
// Function to rotate the falling tetromino piece
function rotate(){
    // Create an array to store the rotated piece
    let rotatedPiece = [];
    // Get the current falling tetromino piece
    let piece = fallingPieceObj.piece;

    // Loop through the rows of the piece
    for(let i=0;i<piece.length;i++){
        // Initialize an array for each row
        rotatedPiece.push([]);
        // Loop through the columns of the row
        for(let j=0;j<piece[i].length;j++){
            // Push 0 to each column of the row
            rotatedPiece[i].push(0);
        }
    }

    // Loop through the rows of the piece
    for(let i=0;i<piece.length;i++){
        // Loop through the columns of the row
        for(let j=0;j<piece[i].length;j++){
            // Transpose the piece by assigning each row to a column and each column to a row
            rotatedPiece[i][j] = piece[j][i];
        }
    }

    // Reverse the rotated piece
    for(let i=0;i<rotatedPiece.length;i++){
        rotatedPiece[i] = rotatedPiece[i].reverse();
    }

    // Check for collision before updating the falling piece
    if(!collision(fallingPieceObj.x,fallingPieceObj.y,rotatedPiece))
        fallingPieceObj.piece = rotatedPiece;

    // Render the updated game
    renderGame();
}

// Function to check for collision between the falling tetromino piece and the grid
function collision(x,y,rotatedPiece){
    // Get the current falling piece or use the rotated piece if it is passed as an argument
    let piece = rotatedPiece || fallingPieceObj.piece;

    // Loop through the rows of the piece
    for(let i=0;i<piece.length;i++){
        // Loop through the columns of the row
        for(let j=0;j<piece[i].length;j++){
            // Check if the cell in the piece is filled
            if(piece[i][j] == 1){
                // Calculate the position of the cell in the grid
                let p = x+j;
                let q = y+i;
                // Check if the cell is within the boundaries of the grid
                if(p>=0 && p<COLS && q>=0 && q<ROWS){
                    // Check if the cell in the grid is filled
                    if(grid[q][p]>0){
                        return true;
                    }
                }else{
                    // Return true if the cell is outside the boundaries of the grid
                    return true;
                }
            }
        }
    }
    // Return false if there is no collision
    return false;
}

// Function that renders the game by filling out the grid with the corresponding colors.
function renderGame() {
    // Iterating through the grid.
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            // Filling the grid with the corresponding color.
            ctx.fillStyle = COLORS[grid[i][j]];
            ctx.fillRect(j, i, 1, 1);
        }
    }

    // Drawing the grid lines
    ctx.strokeStyle = 'rgba(128, 128, 128, 0.5)';
    ctx.lineWidth = 0.025;
    for (let i = 0; i <= ROWS; i++) {
        ctx.beginPath();
        ctx.moveTo(0, i);
        ctx.lineTo(COLS, i);
        ctx.stroke();
    }
    for (let j = 0; j <= COLS; j++) {
        ctx.beginPath();
        ctx.moveTo(j, 0);
        ctx.lineTo(j, ROWS);
        ctx.stroke();
    }

    // Calling the renderPiece function to render the falling piece.
    renderPiece();
}


// Event listener that listens for keydown events and performs the corresponding action.
document.addEventListener("keydown",function(e){
    // Getting the key that was pressed.
    let key = e.key;
    // Checking if the key pressed is ArrowDown and calling the moveDown function.
    if(key == "ArrowDown" & ALLOW_DOWN_KEY==true){
        moveDown();
    }
    // Checking if the key pressed is ArrowLeft and calling the moveLeft function.
    else if(key == "ArrowLeft"){
        moveLeft();
    }
    // Checking if the key pressed is ArrowRight and calling the moveRight function.
    else if(key == "ArrowRight"){
        moveRight();
    }
    // Checking if the key pressed is ArrowUp and calling the rotate function.
    else if(key == "ArrowUp"){
        rotate();
    }
})
