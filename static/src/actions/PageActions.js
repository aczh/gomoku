import * as ACTION from '../constants/ActionConstants'

export function switchPage(page){
    return {type: ACTION.SWITCH_PAGE, page: page}
}
