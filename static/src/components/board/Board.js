import React from 'react'
import { connect } from 'react-redux'
import '../../styles/board.css'
import io from 'socket.io-client'

const socket = io('http://localhost:5000')

class Board extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            p1: new Set(),
            p2: new Set(),
            turns: 0,
            humans: [0],
            // humans: [1, 2],
        }
    }

    move(r, c){
        let index = r * 15 + c
        if (this.state.p1.has(index) || this.state.p2.has(index)){
            return
        }

        socket.emit('move_made', {move: index})
        if (this.state.turns % 2 == 0){
            this.state.p1.add(index)
        } else{
            this.state.p2.add(index)
        }

        this.setState({
            turns: this.state.turns + 1
        })
    }

    render(){

        let board_body = []
        let circles = []
        for (let r = 0; r < 16; r++){
            for (let c = 0; c < 16; c++){
                board_body.push(<div class='cell-lines'></div>)
                if (r < 15 && c < 15){
                    let circleClass = 'circle'
                    if (this.state.p1.has(r * 15 + c)){
                        circleClass = 'circle p1'
                    } else if (this.state.p2.has(r * 15 + c)){
                        circleClass = 'circle p2'
                    }

                    let onClick = ''
                    if (this.state.humans.includes(this.state.turns % 2)){
                        onClick = () => this.move(r, c)
                    }
                    circles.push(<div class={circleClass} onClick={onClick}></div>)
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
}

export default Board
