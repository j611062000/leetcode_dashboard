import './App.css';
import * as React from 'react';
import Badge from 'react-bootstrap/Badge';
import Button from '@mui/material/Button';
import Table from 'react-bootstrap/Table';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { DataGrid } from '@mui/x-data-grid';
import { useDemoData } from '@mui/x-data-grid-generator';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';

const VISIBLE_FIELDS = ['name', 'rating', 'country', 'dateCreated', 'isAdmin'];

function BoxSx() {
  return (
    <Box component="span" sx={{ p: 2, border: '1px dashed grey' }}>
      <Button>Save</Button>
    </Box>
  );
}

function BasicExampleDataGrid() {
  const { data } = useDemoData({
    dataSet: 'Employee',
    visibleFields: VISIBLE_FIELDS,
    rowLength: 100,
  });

  return (
    <div style={{ height: '500', width: '100%' }}>
      <DataGrid {...data} />
    </div>
  );
}



function App() {
  const [problemSet, setProblemSet] = React.useState({ "problems": [] })

  React.useEffect(() => {
    fetch('http://127.0.0.1:5000/problems', { mode: 'cors', contentType: 'application/json' })
      .then(response => response.json())
      .then(responseJson => {
        setProblemSet(responseJson)
      }).catch(error => {
        console.log(error)
      })
  }, [])


  return (
      <div >
        <Container>

        </Container>
        <Container>
        {BasicExampleDataGrid()}

        </Container>
      </div>
  );
}

export default App;
