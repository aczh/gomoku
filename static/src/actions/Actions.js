import * as ACTION from '../constants/ActionConstants'

export function switchPage(page){
    return {type: ACTION.SWITCH_PAGE, page: page}
}

export function updateGame(p1, p2, turns){
    return {type: ACTION.UPDATE_GAME, p1: p1, p2: p2, turns: turns}
}

export function setGameID(game_id){
    return {type: ACTION.SET_GAME_ID, game_id: game_id}
}
