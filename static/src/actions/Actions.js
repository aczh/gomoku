import * as ACTION from '../constants/ActionConstants'

export function switchPage(page){
    return {type: ACTION.SWITCH_PAGE, page: page}
}

export function updateGame(p1, p2, turns, history){
    return {type: ACTION.UPDATE_GAME, p1: p1, p2: p2, turns: turns, history: history}
}

export function setGameID(game_id){
    return {type: ACTION.SET_GAME_ID, game_id: game_id}
}

export function setDialogVisibility(dialog_visibility){
    return {type: ACTION.SET_DIALOG_VISIBILITY, dialog_visibility: dialog_visibility}
}
