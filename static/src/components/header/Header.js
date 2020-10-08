import React from 'react'
import { connect } from 'react-redux'
import { AppBar, Toolbar, MenuIcon, Typography, Button } from '@material-ui/core'
import { switchPage } from '../../actions/Actions'
import '../../styles/header.css'

const Header = ({switchPage}) => {
    return (
        <div className='header'>
            <AppBar position="static">
                <Toolbar>
                    <Button color="inherit" className='header-button' onClick={() => switchPage('about')}>
                        <Typography variant="h6">About</Typography>
                    </Button>
                    <Button color="inherit" className='header-button' onClick={() => switchPage('play')}>
                        <Typography variant="h6">Play</Typography>
                    </Button>
                    <Button color="inherit" className='header-button' onClick={() => switchPage('history')}>
                        <Typography variant="h6">History</Typography>
                    </Button>
                </Toolbar>
            </AppBar>
        </div>
    )
}

const mapStateToProps = state => ({
})
const mapDispatchToProps = dispatch =>({
    switchPage: (page) => dispatch(switchPage(page))
})
export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Header)
