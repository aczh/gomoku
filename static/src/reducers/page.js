import * as ACTION from '../constants/ActionConstants'

const initialState = {
    page: 'play',
}

export default function reducer(state=initialState, action){
    switch (action.type){
        case ACTION.SWITCH_PAGE:
            return {...state, page: action.page}
    }
    return state
}
