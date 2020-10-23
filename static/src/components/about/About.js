import React from 'react'
import {Typography, withStyles} from '@material-ui/core'

import '../../styles/about.css'

const About = ({}) => {
    return (
        <div className='about-text'>
            <Typography className='header-text' variant="h3">
                Gomoku
            </Typography>
            <Typography variant="h5">
                Rules
            </Typography>
            <Typography className='body' variant="body1">
                <p>
                Gomoku is a two player game traditionally played on a 15x15 board.
                Players alternate playing a stone of their color on an empty intersection.
                The first player to make an unbroken chain of 5 stones vertically, diagonally, or horiziontally wins.
                </p>
            </Typography>

            <Typography variant="h5">
                Threats
            </Typography>
            <Typography className='body' variant="body1">
                <p>
                Threats are an important concept in Gomoku.
                Threats are a pattern of pieces on the board that threaten to win the game if not addressed immediately, and thus force a response from the opponent.
                </p>
                <p>
                The strongest threat is the 'open four', an unbroken chain of four pieces of the same color.
                This is a winning threat unless the opponent can win in the next turn, because the opponent cannot block both ends of the threat at once.
                </p>
            </Typography>

            <Typography variant="h5">
                Threat Space Search
            </Typography>
            <Typography className='body' variant="body1">
                <p>
                Against a skilled opponent, winning a game often involves a series of forcing moves which lead to an unblockable threat/multiple threats.
                Victor Allis developed a method called "Threat Space Search" which efficiently finds these forced sequences.
                In his algorithm, Allis allows the opponent to play all available countermoves to a threat, significantly reducing the search space when looking for winning threat sequences.
                </p>
            </Typography>

            <Typography variant="h5">
                Play
            </Typography>
            <Typography className='body' variant="body1">
                <p>
                Try playing against an implementation of Threat Space Search by clicking the 'Play' button on the top of the screen. The AI will play the blue pieces and you can place down your red pieces by clicking on an empty intersection.
                </p>
                <p>
                The AI moves first.
                </p>
            </Typography>

            <Typography variant="h5">
                Implementation
            </Typography>
            <Typography className='body' variant="body1">
                <p>
                The code involved in programming the Threat Space Search AI, as well as the frontend/backend code involved in hosting this website can be accessed by clicking on the Github icon in the top right. A link to my LinkedIn is also available on the top right of the screen.
                </p>
            </Typography>
        </div>
    )
}

export default About
