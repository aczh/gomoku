import React from 'react'
import { connect } from 'react-redux'
import { TextField, Button } from '@material-ui/core'
import Board from './Board'
import Sidebar from './Sidebar'
import '../../styles/game.css'

import io from 'socket.io-client'

const socket = io(process.env.API_URL)

const Game = ({}) => {
    return (
        <div className='flex-container'>
            <Board socket={socket}/>
            <Sidebar socket={socket}/>
        </div>
    )
}

const mapStateToProps = state => ({
})

export default connect(mapStateToProps, null)(Game)
