import { combineReducers } from 'redux'
import page from '../reducers/page'
import game from '../reducers/game'
import user from '../reducers/user'

const rootReducer = combineReducers({
    user,
    game,
    page,
})
export default rootReducer
