import React from 'react'
import { AppBar, Typography, Button, Tabs, Tab, Box, IconButton } from '@material-ui/core'
import GitHubIcon from '@material-ui/icons/GitHub'
import LinkedInIcon from '@material-ui/icons/LinkedIn'
import Game from '../game'
import About from '../about'
import '../../styles/landing.css'

function TabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`simple-tabpanel-${index}`}
            {...other}
        >
            {
                value === index && (
                <Box p={3}>
                    {children}
                </Box>
                )
            }
        </div>
    )
}

const Landing = ({}) => {
    const [value, setValue] = React.useState(0);
    function handleChange(event, newValue){
        setValue(newValue);
    }

    const ButtonInTabs = ({ className, onClick, children }) => {
        return (
            <div className='icons'>
                <IconButton color="inherit" href='https://www.linkedin.com/in/allenczhang/'>
                    <LinkedInIcon />
                </IconButton>
                <IconButton color="inherit" href='https://github.com/aczh/gomoku'>
                    <GitHubIcon />
                </IconButton>
            </div>
        )
    };

    return (
        <div className='header'>
            <AppBar position="static" className='header-appbar'>
                <Tabs value={value} onChange={handleChange}>
                    <Tab label={
                        <Typography variant="h6">About</Typography>
                    }/>
                    <Tab label={
                        <Typography variant="h6">Play</Typography>
                    }/>

                    <ButtonInTabs/>
                </Tabs>

            </AppBar>
            <TabPanel value={value} index={0}>
                <About/>
            </TabPanel>
            <TabPanel value={value} index={1}>
                <Game/>
            </TabPanel>
        </div>
    )
}

export default Landing
