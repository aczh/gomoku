import React from 'react'
import {Accordion, AccordionSummary, AccordionDetails, Typography} from '@material-ui/core'
import '../../styles/about.css'

const About = ({}) => {
    const [open, setOpen] = React.useState(true);
    const handleClick = () => {
      setOpen(!open);
    }

    return (
        <div>
            <Accordion>
                <AccordionSummary>
                    <Typography>Instructions</Typography>
                </AccordionSummary>
                <AccordionDetails>
                    Gomoku is a two player game traditionally played on a 15x15 board. Players alternate playing a stone of their color on an empty intersection. The first player to make an unbroken chain of 5 stones vertically, diagonally, or horiziontally wins.
                </AccordionDetails>

            </Accordion>
        </div>
    )
//     <Accordion>
// </Accordion>
// <Accordion>
//   <AccordionSummary
//     expandIcon={<ExpandMoreIcon />}
//     aria-controls="panel2a-content"
//     id="panel2a-header"
//   >
//     <Typography>Accordion 2</Typography>
//   </AccordionSummary>
//   <AccordionDetails>
//     <Typography>
//       Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
//       sit amet blandit leo lobortis eget.
//     </Typography>
//   </AccordionDetails>
// </Accordion>
// <Accordion disabled>
//   <AccordionSummary
//     expandIcon={<ExpandMoreIcon />}
//     aria-controls="panel3a-content"
//     id="panel3a-header"
//   >
//     <Typography>Disabled Accordion</Typography>
//   </AccordionSummary>
// </Accordion>
}

export default About
