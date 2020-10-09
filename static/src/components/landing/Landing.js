import React from 'react'
import { connect } from 'react-redux'
import Game from '../game'
import About from '../about'

const Landing = ({page}) => {
    let contents = `Invalid page ${page}`
    switch (page){
        case 'about':
            contents = <About/>
            break
        case 'play':
            contents = <Game/>
            break
    }
    return (
        <div>{contents}</div>
    )
}


const mapStateToProps = state => ({
    page: state.page.page
})

export default connect(mapStateToProps, null)(Landing)
