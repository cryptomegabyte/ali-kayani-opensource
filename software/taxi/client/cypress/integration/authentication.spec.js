describe('Authentication', function () {
  const logIn = () => {
    const { username, password } = Cypress.env('credentials');
    cy.intercept('POST', 'log_in', {
      statusCode: 200,
      body: {
        'access': 'ACCESS_TOKEN',
        'refresh': 'REFRESH_TOKEN'
      }
    }).as('logIn');
  
    cy.visit('/#/log-in');
    cy.get('input#username').type(username);
    cy.get('input#password').type(password, { log: false });
    cy.get('button').contains('Log in').click();
    cy.wait('@logIn');
  };

  it('Can log in.', function () {
    cy.visit('/#/log-in');
    cy.get('input#username').type('a.user@foo.bar.com');
    cy.get('input#password').type('pAssw0rd', { log: false });
    cy.get('button').contains('Log in').click();
    cy.hash().should('eq', '#/');
  });

  it('Can sign up.', function () {
    cy.visit('/#/sign-up');
    cy.get('input#username').type('a.user@foo.bar.com');
    cy.get('input#firstName').type('Foo');
    cy.get('input#lastName').type('Bar');
    cy.get('input#password').type('pAssw0rd', { log: false });
    cy.get('select#group').select('driver');
    cy.get('input#photo').attachFile('images/photo.jpg');
    cy.get('button').contains('Sign up').click();
    cy.hash().should('eq', '#/log-in');
  });

  it('Can log in.', function () {
    logIn();
    cy.hash().should('eq', '#/');
    cy.get('button').contains('Log out');
  });

  it('Cannot visit the sign up page when logged in.', function () {
    logIn();
    cy.visit('/#/sign-up');
    cy.hash().should('eq', '#/');
  });

  it('Cannot visit the login page when logged in.', function () {
    logIn();
    cy.visit('/#/log-in');
    cy.hash().should('eq', '#/');
  });

  it('Cannot see links when logged in.', function () {
    logIn();
    cy.get('button#signUp').should('not.exist');
    cy.get('button#logIn').should('not.exist');
  });
});
  