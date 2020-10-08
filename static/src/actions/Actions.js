import * as ACTION from '../constants/ActionConstants'

export function switchPage(page){
    return {type: ACTION.SWITCH_PAGE, page: page}
}

export function updateGame(p1, p2, turns){
    return {type: ACTION.UPDATE_GAME, p1: p1, p2: p2, turns: turns}
}

export function login(username){
    return {type: ACTION.LOGIN, username: username}
}
