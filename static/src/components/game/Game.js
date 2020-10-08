import React from 'react'
import { connect } from 'react-redux'
import { TextField, Button } from '@material-ui/core'
import Board from './Board'
import Login from '../login'

const Game = ({username}) => {
    let contents = <Board username={username}/>
    if (username === null){
        contents = <Login/>
    }

    return (
        <div>{contents}</div>
    )
}

const mapStateToProps = state => ({
    username: state.user.username
})
const mapDispatchToProps = dispatch =>({
})
export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Game)
