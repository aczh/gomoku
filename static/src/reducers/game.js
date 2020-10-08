import * as ACTION from '../constants/ActionConstants'

const initialState = {
    p1: '0',
    p2: '0',
    turns: 0,
}

export default function reducer(state=initialState, action){
    switch (action.type){
        case ACTION.UPDATE_GAME:
            return {...state, p1: action.p1, p2: action.p2, turns: action.turns}
    }
    return state
}
