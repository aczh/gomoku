import * as ACTION from '../constants/ActionConstants'
import axios from 'axios';

export function updateGame(p1, p2, turns, history){
    return {type: ACTION.UPDATE_GAME, p1: p1, p2: p2, turns: turns, history: history}
}

export function setDialogVisibility(dialog_visibility){
    return {type: ACTION.SET_DIALOG_VISIBILITY, dialog_visibility: dialog_visibility}
}
