import { tripResponse } from "../support/rider.test.data";
const faker = require("faker");

const driverEmail = faker.internet.email();
const driverFirstName = faker.name.firstName();
const driverLastName = faker.name.lastName();
const riderEmail = faker.internet.email();
const riderFirstName = faker.name.firstName();
const riderLastName = faker.name.lastName();

describe("The rider dashboard", function () {
  before(function () {
    cy.addUser(riderEmail, riderFirstName, riderLastName, "rider");
    cy.addUser(driverEmail, driverFirstName, driverLastName, "driver");
  });

  it("Displays current and completed trips", function () {
    cy.intercept("trip", {
      statusCode: 200,
      body: tripResponse,
    }).as("getTrips");

    cy.logIn(riderEmail);

    cy.visit("/#/rider");
    cy.wait("@getTrips");

    // Current trips.
    cy.get("[data-cy=trip-card]").eq(0).contains("STARTED");

    // Completed trips.
    cy.get("[data-cy=trip-card]").eq(1).contains("COMPLETED");
  });

  it("Cannot be visited if the user is not a rider", function () {
    cy.intercept("POST", "log_in").as("logIn");

    cy.logIn(driverEmail);

    cy.visit("/#/rider");
    cy.hash().should("eq", "#/");
  });

  it("Can be visited if the user is a rider", function () {
    cy.intercept("POST", "log_in").as("logIn");

    cy.logIn(riderEmail);

    cy.visit("/#/rider");
    cy.hash().should("eq", "#/rider");
  });
  it("Displays messages for no trips", function () {
    cy.intercept("trip", {
      statusCode: 200,
      body: [],
    }).as("getTrips");

    cy.logIn(riderEmail);

    cy.visit("/#/rider");
    cy.wait("@getTrips");

    // Current trips.
    cy.get("[data-cy=trip-card]").eq(0).contains("No trips.");

    // Completed trips.
    cy.get("[data-cy=trip-card]").eq(1).contains("No trips.");
  });
  it("Shows details about a trip", () => {
    cy.intercept("/api/trip/*", {
      statusCode: 200,
      body: tripResponse[0],
    }).as("getTrip");

    cy.logIn(riderEmail);

    cy.visit(`/#/rider/${tripResponse[0].id}`);
    cy.wait("@getTrip");

    cy.get("[data-cy=trip-card]")
      .should("have.length", 1)
      .and("contain.text", "STARTED");
  });
  it("Can request a new trip", function () {
    cy.intercept("trip").as("getTrips");

    cy.logIn(riderEmail);

    cy.visit("/#/rider/request");

    cy.get("[data-cy=pick-up-address]").type("123 Main Street");
    cy.get("[data-cy=drop-off-address]").type("456 South Street");
    cy.get("[data-cy=submit]").click();

    cy.wait("@getTrips");
    cy.hash().should("eq", "#/rider");
  });
});
