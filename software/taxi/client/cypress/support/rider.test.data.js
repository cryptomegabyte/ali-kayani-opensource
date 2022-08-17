const faker = require("faker");

const driverFirstName = faker.name.firstName();
const driverLastName = faker.name.lastName();
const riderFirstName = faker.name.firstName();
const riderLastName = faker.name.lastName();

export const tripResponse = [
  {
    id: "23033964-f2ca-4150-bb8c-4a1182c3737d",
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
    id: "2ee84fb5-f3c4-4aff-9677-b6476156d3bf",
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
