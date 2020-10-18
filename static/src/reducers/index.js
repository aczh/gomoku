import { combineReducers } from 'redux'
import page from '../reducers/page'
import game from '../reducers/game'

const rootReducer = combineReducers({
    game,
    page,
})
export default rootReducer
