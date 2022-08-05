describe('Authentication', function () {
    it('Can log in.', function () {
      cy.visit('/#/log-in');
      cy.get('input#username').type('a.user@foo.bar.com');
      cy.get('input#password').type('pAssw0rd', { log: false });
      cy.get('button').contains('Log in').click();
      cy.hash().should('eq', '#/');
    });
  });