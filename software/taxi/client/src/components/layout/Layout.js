import React from "react";
import { LinkContainer } from "react-router-bootstrap";
import { Outlet } from "react-router-dom";
import { Button, Container, Form, Nav, Navbar } from "react-bootstrap";
import { isRider } from "../../services/AuthService";

function Layout({ isLoggedIn, logOut }) {
  return (
    <>
      <Navbar bg="light" expand="lg" variant="light">
        <Container>
          <LinkContainer to="/">
            <Navbar.Brand className="logo">Taxi</Navbar.Brand>
          </LinkContainer>
          <Navbar.Toggle />
          <Navbar.Collapse>
            {isRider() && (
              <Nav className="me-auto">
                <LinkContainer to="/rider/request">
                  <Nav.Link data-cy="request-trip">Request a trip</Nav.Link>
                </LinkContainer>
              </Nav>
            )}
            {isLoggedIn && (
              <Form className="ms-auto">
                <Button type="button" onClick={() => logOut()}>
                  Log out
                </Button>
              </Form>
            )}
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <Container className="pt-3">
        <Outlet />
      </Container>
    </>
  );
}

export default Layout;
