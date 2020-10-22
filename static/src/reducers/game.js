import * as ACTION from '../constants/ActionConstants'

const initialState = {
    p1: '0',
    p2: '0',
    turns: 0,
    history: [],
    dialog_visibility: false,
}

export default function reducer(state=initialState, action){
    switch (action.type){
        case ACTION.UPDATE_GAME:
            return {...state, p1: action.p1, p2: action.p2, turns: action.turns, history: action.history}
        case ACTION.SET_DIALOG_VISIBILITY:
            return {...state, dialog_visibility: action.dialog_visibility}
    }
    return state
}
