import React from 'react'
import { connect } from 'react-redux'
import '../../styles/board.css'

const Board = () => {
    let board_body = []
    let clickable = []
    let circles = []
    for (let r = 0; r < 16; r++){
        for (let c = 0; c < 16; c++){
            board_body.push(<div class='cell-lines'></div>)
            if (r < 15 && c < 15){
                circles.push(<div class='circle' onClick={() => console.log(`${r}, ${c}`)}></div>)
            }
        }
    }

    return (
        <div>
            <div class='board-grid lines'>
                {board_body}
            </div>
            <div class='board-grid pieces'>
                {circles}
            </div>
        </div>
    )
}

export default Board
