import * as ACTION from '../constants/ActionConstants'

const initialState = {
    p1: '0',
    p2: '0',
    turns: 0,
    game_id: null,
}

export default function reducer(state=initialState, action){
    switch (action.type){
        case ACTION.UPDATE_GAME:
            return {...state, p1: action.p1, p2: action.p2, turns: action.turns}
        case ACTION.SET_GAME_ID:
            return {...state, game_id: action.game_id}
    }
    return state
}
