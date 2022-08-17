const faker = require("faker");

const driverFirstName = faker.name.firstName();
const driverLastName = faker.name.lastName();
const riderFirstName = faker.name.firstName();
const riderLastName = faker.name.lastName();

export const tripResponse = [
  {
    id: "94fc5eba-de7a-44b2-8000-856ec824609d",
    created: "2020-08-18T21:41:08.112946Z",
    updated: "2020-08-18T21:41:08.112986Z",
    pick_up_address: "A",
    drop_off_address: "B",
    status: "STARTED",
    driver: {
      id: 113,
      first_name: driverFirstName,
      last_name: driverLastName,
      photo: "http://localhost:8003/media/photos/photo_QI0TTYh.jpg",
    },
    rider: {
      id: 112,
      first_name: riderFirstName,
      last_name: riderLastName,
      photo: "http://localhost:8003/media/photos/photo_r3XrvgH.jpg",
    },
  },
  {
    id: "bb3042cd-88dd-472c-890f-c5f59481de01",
    created: "2020-08-18T21:41:08.112946Z",
    updated: "2020-08-18T21:41:08.112986Z",
    pick_up_address: "A",
    drop_off_address: "B",
    status: "REQUESTED",
    driver: {
      id: 113,
      first_name: driverFirstName,
      last_name: driverLastName,
      photo: "http://localhost:8003/media/photos/photo_QI0TTYh.jpg",
    },
    rider: {
      id: 112,
      first_name: riderFirstName,
      last_name: riderLastName,
      photo: "http://localhost:8003/media/photos/photo_r3XrvgH.jpg",
    },
  },
  {
    id: "50e0034f-0696-4b26-9068-8a7d064db922",
    created: "2020-08-18T21:41:08.112946Z",
    updated: "2020-08-18T21:41:08.112986Z",
    pick_up_address: "A",
    drop_off_address: "B",
    status: "COMPLETED",
    driver: {
      id: 113,
      first_name: driverFirstName,
      last_name: driverLastName,
      photo: "http://localhost:8003/media/photos/photo_QI0TTYh.jpg",
    },
    rider: {
      id: 112,
      first_name: riderFirstName,
      last_name: riderLastName,
      photo: "http://localhost:8003/media/photos/photo_r3XrvgH.jpg",
    },
  },
];
