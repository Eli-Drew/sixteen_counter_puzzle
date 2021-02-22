/*
=================================================
Author:   Drew Rinker
Date:     02/21/21

Notes:    This is just a prototype. My JS skills
          aren't up to par at the moment. The 
          purpose of this page is to help with 
          that.
=================================================
*/

function singleMove(board, x, y) {
    if (board[x][y] == 0) {
        board[x][y] = 1;
    } else {
        board[x][y] = 0;
    }
    if (board[x][y + 1] == 0) {
        board[x][y + 1] = 1;
    } else {
        board[x][y + 1] = 0;
    }
    if (board[x + 1][y] == 0) {
        board[x + 1][y] = 1;
    } else {
        board[x + 1][y] = 0;
    }
    if (board[x + 1][y + 1] == 0) {
        board[x + 1][y + 1] = 1;
    } else {
        board[x + 1][y + 1] = 0;
    }
    return board;
}

//model
function createGameBoard(rows, cols) {
    var board = [];
    var boardRow = [];
    for (let x = 0; x < rows; x++) {
        for (let i = 0; i < cols; i++) {
            boardRow.push(0);
        }
        board.push(boardRow);
        boardRow = []
    }

    return board;
}

function main() {
    var rows = 4;
    var columns = 4;
    var gameBoard = createGameBoard(rows, columns);
}