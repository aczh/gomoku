import React from 'react'
import { connect } from 'react-redux'
import '../../styles/board.css'


export default class Board extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            p1: '0',
            p2: '0',
            turns: 0,
            should_move: false,
        }

    }

    componentDidMount(){
        this.props.socket.on('request_move', (data) => {
            this.setState({
                p1: data.p1,
                p2: data.p2,
                turns: data.turns,
                should_move: true
            })
        })
        this.props.socket.on('game_won', (data) => {
            this.setState({
                p1: data.p1,
                p2: data.p2,
                turns: data.turns,
                should_move: false
            })
        })
    }

    componentWillUnmount(){
        this.props.socket.off('request_move')
        this.props.socket.off('game_won')
    }

    valid_move = (index) => {
        if (index <= this.state.p1.length && this.state.p1.charAt(index) == '1'){ return false }
        if (index <= this.state.p2.length && this.state.p1.charAt(index) == '1'){ return false }
        return true
    }

    make_move = (index) => {
        let p1 = this.state.p1
        let p2 = this.state.p2
        if (this.state.turns % 2 == 0){
            if (index > this.state.p1.length){
                p1 += '0'.repeat(index - this.state.p1.length)
            }
            p1 = p1.substring(0, index) + '1' + p1.substring(index + 1)
        } else{
            if (index > this.state.p2.length){
                p2 += '0'.repeat(index - this.state.p2.length)
            }
            p2 = p2.substring(0, index) + '1' + p2.substring(index + 1)
        }
        this.setState({
            p1: p1,
            p2: p2,
        })
    }

    move(index){
        if (this.valid_move(index)){
            this.make_move(index)
            this.props.socket.emit('move_made', {move: index})
        }
    }

    render(){
        let board_body = []
        for (let r = 0; r < 16; r++){
            for (let c = 0; c < 16; c++){
                board_body.push(<div key={`line${r} ${c}`} className='cell-lines'></div>)
            }
        }

        let circles = []
        for (let index = 0; index < 225; index++){
            let circleClass = 'circle'
            if (index <= this.state.p1.length && this.state.p1.charAt(index) == '1'){
                circleClass = 'circle p1'
            } else if (index <= this.state.p2.length && this.state.p2.charAt(index) == '1'){
                circleClass = 'circle p2'
            }

            let onClick = null
            if (this.state.should_move){
                onClick = () => this.move(index)
            }
            circles.push(<div key={`piece${index}`} className={circleClass} onClick={onClick}></div>)
        }

        return (
            <div className='board'>
                <div className='board-grid lines'>
                    {board_body}
                </div>
                <div className='board-grid pieces'>
                    {circles}
                </div>
            </div>
        )

    }
}
