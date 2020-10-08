import React from 'react'
import { connect } from 'react-redux'
import Game from '../game'
import About from '../about'

const Landing = ({page}) => {
    let contents = null
    if (page == 'about'){
        contents = <About/>
    } else if (page == 'play'){
        contents = <Game/>
    } else{
        contents = `Invalid page ${page}`
    }
    return (
        <div>{contents}</div>
    )
}


const mapStateToProps = state => ({
    page: state.page.page
})

export default connect(mapStateToProps, null)(Landing)
