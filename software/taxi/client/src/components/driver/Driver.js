import React, { useState, useEffect } from "react";
import { Breadcrumb } from "react-bootstrap";
import { Navigate } from "react-router-dom";

import { isDriver } from "../../services/AuthService";
import { getTrips } from "../../services/TipService";
import TripCard from "../trip_card/TripCard";

function Driver(props) {
  // new
  const [trips, setTrips] = useState([]);

  // new
  useEffect(() => {
    const loadTrips = async () => {
      const { response, isError } = await getTrips();
      if (isError) {
        setTrips([]);
      } else {
        setTrips(response.data);
      }
    };
    loadTrips();
  }, []);

  if (!isDriver()) {
    return <Navigate to="/" />;
  }

  // new
  const getCurrentTrips = () => {
    return trips.filter((trip) => {
      return trip.driver !== null && trip.status !== "COMPLETED";
    });
  };

  // new
  const getRequestedTrips = () => {
    return trips.filter((trip) => {
      return trip.status === "REQUESTED";
    });
  };

  // new
  const getCompletedTrips = () => {
    return trips.filter((trip) => {
      return trip.status === "COMPLETED";
    });
  };
  return (
    <>
      <Breadcrumb>
        <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
        <Breadcrumb.Item active>Dashboard</Breadcrumb.Item>
      </Breadcrumb>

      <TripCard
        title="Current Trip"
        trips={getCurrentTrips()}
        group="driver"
        otherGroup="rider"
      />

      <TripCard
        title="Requested Trips"
        trips={getRequestedTrips()}
        group="driver"
        otherGroup="rider"
      />

      <TripCard
        title="Recent Trips"
        trips={getCompletedTrips()}
        group="driver"
        otherGroup="rider"
      />
    </>
  );
}

export default Driver;
