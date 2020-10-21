import React from 'react'
import { connect } from 'react-redux'
import '../../styles/board.css'
import { updateGame } from '../../actions/Actions'

const Board = ({socket, updateGame, p1, p2, turns, history}) => {
    const move = (index) => {
        if (valid_move(index)){
            make_move(index)
            socket.emit('move_made', {move: index})
        }
    }

    const valid_move = (index) => {
        if (index <= p1.length && p1.charAt(index) == '1'){ return false }
        if (index <= p2.length && p1.charAt(index) == '1'){ return false }
        return true
    }

    const make_move = (index) => {
        if (turns % 2 == 0){
            if (index > p1.length){
                p1 += '0'.repeat(index - p1.length)
            }
            p1 = p1.substring(0, index) + '1' + p1.substring(index + 1)
        } else{
            if (index > p2.length){
                p2 += '0'.repeat(index - p2.length)
            }
            p2 = p2.substring(0, index) + '1' + p2.substring(index + 1)
        }
        updateGame(p1, p2, turns + 1, [...history, [Math.floor(index / 15), index % 15]])
    }

    const construct_board = () => {
        let board_body = []
        for (let r = 0; r < 16; r++){
            for (let c = 0; c < 16; c++){
                board_body.push(<div key={`line${r} ${c}`} className='cell-lines'></div>)
            }
        }
        return board_body
    }

    const construct_pieces = () => {
        let circles = []
        for (let index = 0; index < 225; index++){
            let circleClass = 'circle'
            if (index <= p1.length && p1.charAt(index) == '1'){ circleClass = 'circle p1' }
            else if (index <= p2.length && p2.charAt(index) == '1'){ circleClass = 'circle p2' }

            try{
                if (index === history[history.length - 1][0] * 15 + history[history.length - 1][1]){
                    circleClass += ' highlight'
                }
            } catch{}


            let onClick = null
            if (turns % 2 === 1){
                onClick = () => move(index)
            }
            circles.push(<div key={`piece${index}`} className={circleClass} onClick={onClick}></div>)
        }
        return circles
    }

    return (
        <div className='board'>
            <div className='board-grid lines'>
                {construct_board()}
            </div>
            <div className='board-grid pieces'>
                {construct_pieces()}
            </div>
        </div>
    )
}

const mapStateToProps = state => ({
    p1: state.game.p1,
    p2: state.game.p2,
    turns: state.game.turns,
    history: state.game.history,
})
const mapDispatchToProps = dispatch =>({
    updateGame: (p1, p2, turns, history) => dispatch(updateGame(p1, p2, turns, history))
})
export default connect(mapStateToProps, mapDispatchToProps)(Board)
