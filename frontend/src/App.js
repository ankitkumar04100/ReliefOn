import React from 'react';
import MapView from './components/MapView';
import RequestForm from './components/RequestForm';
import VolunteerDashboard from './components/VolunteerDashboard';

function App() {
  return (
    <div className="App">
      <h1 className="text-3xl font-bold text-center mt-5">ReliefOn</h1>
      <RequestForm />
      <MapView />
      <VolunteerDashboard />
    </div>
  );
}

export default App;
