import * as ACTION from '../constants/ActionConstants'

const initialState = {
    p1: '0',
    p2: '0',
    turns: 0,
    history: [],
    game_id: null,
    dialog_visibility: false,
}

export default function reducer(state=initialState, action){
    switch (action.type){
        case ACTION.UPDATE_GAME:
            return {...state, p1: action.p1, p2: action.p2, turns: action.turns, history: action.history}
        case ACTION.SET_GAME_ID:
            return {...state, game_id: action.game_id}
        case ACTION.SET_DIALOG_VISIBILITY:
            console.log("VISIBILITY SET")
            console.log(action.dialog_visibility)
            return {...state, dialog_visibility: action.dialog_visibility}
    }
    return state
}
