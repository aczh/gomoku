import React from 'react'
import {Typography} from '@material-ui/core'

import '../../styles/about.css'

const About = ({}) => {
    return (
        <div className='about-text'>
            <Typography className='header' variant="h5">
                Instructions
            </Typography>
            <Typography className='body' variant="body1">
                Gomoku is a two player game traditionally played on a 15x15 board.
                Players alternate playing a stone of their color on an empty intersection.
                The first player to make an unbroken chain of 5 stones vertically, diagonally, or horiziontally wins.
            </Typography>

            <Typography className='header' variant="h5">
                Threats
            </Typography>
            <Typography className='body' variant="body1">
                Threats are an important concept in Gomoku.
                Threats are a pattern of pieces on the board that threaten to win the game if not addressed immediately.
                The strongest threat is the 'open four', an unbroken chain of four pieces of the same color.
                This is a winning threat unless the opponent can win in the next turn, because the opponent cannot block both ends of the threat at once.
            </Typography>

            <Typography className='header' variant="h5">
                Threat Space Search
            </Typography>
            <Typography className='body' variant="body1">
                Against a skilled opponent, winning a game often involves a series of forcing moves which lead to an unblockable threat.
                Victor Allis developed a method called "Threat Space Search" which efficiently finds these forced sequences.
                In his algorithm, Allis allows the opponent to play all available countermoves to a threat, significantly reducing the search space when looking for winning threat sequences.
            </Typography>
        </div>
    )
}

export default About
