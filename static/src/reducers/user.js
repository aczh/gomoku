import * as ACTION from '../constants/ActionConstants'

const initialState = {
    username: null
}
export default function reducer(state=initialState, action){
    switch (action.type){
        case ACTION.LOGIN:
            return {...state, username: action.username}
    }
    return state
}
