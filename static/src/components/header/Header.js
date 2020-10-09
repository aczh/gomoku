import React from 'react'
import { connect } from 'react-redux'
import { AppBar, Toolbar, MenuIcon, Typography, Button } from '@material-ui/core'
import { switchPage, logout } from '../../actions/Actions'
import '../../styles/header.css'

const Header = ({switchPage, logout}) => {
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
                    <Button color="inherit" style={{marginLeft: 'auto'}} onClick={() => logout()}>
                        Logout
                    </Button>
                </Toolbar>
            </AppBar>
        </div>
    )
}

const mapStateToProps = state => ({
    username: state.user.username
})

const mapDispatchToProps = dispatch =>({
    switchPage: (page) => dispatch(switchPage(page)),
    logout: () => dispatch(logout()),
})
export default connect(mapStateToProps, mapDispatchToProps)(Header)
