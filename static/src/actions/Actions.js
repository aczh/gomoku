import * as ACTION from '../constants/ActionConstants'
import axios from 'axios';
import io from 'socket.io-client'

export const socket = io(process.env.API_URL)

export function switchPage(page){
    return {type: ACTION.SWITCH_PAGE, page: page}
}

export function updateGame(p1, p2, turns, history){
    return {type: ACTION.UPDATE_GAME, p1: p1, p2: p2, turns: turns, history: history}
}

export function setDialogVisibility(dialog_visibility){
    return {type: ACTION.SET_DIALOG_VISIBILITY, dialog_visibility: dialog_visibility}
}

export function newGame(){
    return dispatch => {
        axios.post(`${process.env.API_URL}/game`).then(res => {
                let game_id = res.data._id.$oid
                dispatch({type: ACTION.NEW_GAME, game_id: game_id})
                socket.emit('start_game', {game_id: game_id})
            })

    }
}
