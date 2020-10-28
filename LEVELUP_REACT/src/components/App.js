import React from 'react';
import Click from './Click';
import Essay from './Essay';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';




class App extends React.Component {
   

    render() {
      return(
        <div> 
             <Typography align='center' variant="h2" gutterBottom>
                 Level Up
             </Typography>
            
            
            <Grid container justify="center" spacing={3}>
                <Grid item xs={4}>
                    <Essay />     
                </Grid>
                
                <Grid item xs={2}>
                    <Click />
                </Grid>    
            </Grid>
            
            
        </div>
       
      );
    }
  }

  export default App;
  