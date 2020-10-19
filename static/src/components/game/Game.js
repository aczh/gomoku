import React from 'react'
import { connect } from 'react-redux'
import { TextField, Button } from '@material-ui/core'
import Board from './Board'
import Sidebar from './Sidebar'

import io from 'socket.io-client'

const socket = io('http://localhost:80')

const Game = ({}) => {
    return (
        <div>
            <Board socket={socket}/>
            <Sidebar socket={socket}/>
        </div>
    )
}

const mapStateToProps = state => ({
})

export default connect(mapStateToProps, null)(Game)
