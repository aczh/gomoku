import React from 'react'
import { AppBar, Typography, Button, Tabs, Tab, Box } from '@material-ui/core'
import Game from '../game'
import About from '../about'
import '../../styles/header.css'

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

    return (
        <div className='header'>
            <AppBar position="static" className='header-appbar'>
                <Tabs value={value} onChange={handleChange}>
                    <Tab label={
                        <Typography component={'div'} variant="h6">About</Typography>
                    }/>
                    <Tab label={
                        <Typography component={'div'} variant="h6">Play</Typography>
                    }/>
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
