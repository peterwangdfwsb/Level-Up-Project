import React from 'react';
import Chart from "react-google-charts";
import Button from '@material-ui/core/Button';
import './Click.css';







class Click extends React.Component {
    constructor(props){
        super(props)
        this.state = {
                data: '',
                Type:'',
                format:''
        }
        this.onClick1 = this.onClick1.bind(this);
        this.onClick2 = this.onClick2.bind(this);
    }
    onClick1 = () => {
        fetch('/db.json',{method:'GET'})
        .then(response => response.json())
        .then((jsonData) => {
            let level_dict=jsonData;
            let level_keys=Object.keys(level_dict);
            var levelinformat=[['LEVEL','DETECTION','LEVEL_PATH','SUGGESTION']];
            console.log(level_keys);
            for (var i=0;i<Object.keys(level_dict).length;i++){
                let onlyloop=[];
                onlyloop.push(level_keys[i]);
                onlyloop.push(level_dict[level_keys[i]][0]);
                onlyloop.push({v:Number(level_dict[level_keys[i]][1]),f:level_dict[level_keys[i]][2].split(' | ')[0]});
                onlyloop.push(level_dict[level_keys[i]][2].split(' | ')[1]);
                levelinformat.push(onlyloop);
                console.log(levelinformat);
            }
            this.setState({ data:levelinformat,
                Type:"Table",
                format:[
                  {type: 'ArrowFormat',
                  column: 2
                  },
                ]
            });
            



        });

        
       
       
    }
    onClick2 = () => {
        fetch('/db.json',{method:'GET'})
        .then(response => response.json())
        .then((jsonData) => {
            let level_dict=jsonData;
            let level_keys=Object.keys(level_dict);
            let level_pie={'A1':0,'A2':0,'B1':0,'B3':0,'C1':0,'C2':0};
            for(var i=0;i<=level_keys.length-1;i++){
                if(level_keys[i].split('_')[0]==='A1'){
                level_pie['A1']+=1;
                }
                else if(level_keys[i].split('_')[0]==='A2'){
                level_pie['A2']+=1;
                }
                else if(level_keys[i].split('_')[0]==='B1'){
                level_pie['B1']+=1;
                }
                else if(level_keys[i].split('_')[0]==='B2'){
                level_pie['B2']+=1;
                }
                else if(level_keys[i].split('_')[0]==='C1'){
                level_pie['C1']+=1;
                }
                else if(level_keys[i].split('_')[0]==='C2'){
                level_pie['C2']+=1;
                }}

            let pie_key=Object.keys(level_pie);
            var pie_total=[['Level','Number']];
            for(var j=0;j<=pie_key.length-1;j++){
                let onlyinloop=[];
                onlyinloop.push(pie_key[j]);
                onlyinloop.push(Number(level_pie[pie_key[j]]));
                pie_total.push(onlyinloop);
                }

            this.setState({ data:pie_total,
                Type:"PieChart",
                format:''
            });    
        })
    }
    render() {
        let chart_test;
        if(this.state.format.length>0){
            chart_test= <Chart className='chart_tag'
            width={'500px'}
            height={'300px'}
            chartType={this.state.Type}
            loader={<div>Loading Chart</div>}
            data={this.state.data}
            formatters={this.state.format}
            />;
        }
        else{
            chart_test=<Chart className='chart_tag'
            width={'500px'}
            height={'300px'}
            chartType={this.state.Type}
            loader={<div>Loading Chart</div>}
            data={this.state.data}
            />;
        }
      



        return (
            <div className='ana_tag'>
               
                
                <Button variant="outlined" color="primary" id="btn1" onClick={() => { this.onClick1() }}>
                    ANALYZE
                </Button>{' '}
                <Button variant="outlined" color="primary" id="btn2" onClick={() => { this.onClick2() }}>
                    PIE
                </Button>
                {this.state.data.length > 0 && chart_test
                }
                
                
                
                
                
                
            </div >
        )
    }
}
export default Click;