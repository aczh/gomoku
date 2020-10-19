import React from 'react'
import { connect } from 'react-redux'
import { TextField, Button } from '@material-ui/core'
import Board from './Board'
import Sidebar from './Sidebar'
import {AWS_URL} from '../../constants/UrlConstants'
import '../../styles/game.css'

import io from 'socket.io-client'

const socket = io(AWS_URL)

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
