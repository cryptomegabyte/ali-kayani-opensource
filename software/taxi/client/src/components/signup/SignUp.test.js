import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import SignUp from './SignUp';

Enzyme.configure({adapter: new Adapter()});

let wrapper;

beforeEach(() => {
    wrapper = shallow(<SignUp />);
  });

it('should render the SignUp component', () => {
    expect(wrapper).toBeTruthy();
  });

it('should render the Breadcrumb component', () => {
  expect(wrapper.find('Breadcrumb')).toBeTruthy();
});

it('the Breadcrumb component should have 2 children', () => {
  expect(wrapper.find('Breadcrumb').children()).toHaveLength(2);
});

it('should render the Card component', () => {
  expect(wrapper.find('Card')).toBeTruthy();
});

it('the Card component should have 2 children', () => {
  expect(wrapper.find('Card').children()).toHaveLength(2);
});

it('CardHeader should have text', () => {
  const card = wrapper.find('Card').children().at(0);
  const cardHeader = card.children().at(0).text();
  expect(cardHeader == 'Sign up')
});

it('CardText should have text', () => {
  const card = wrapper.find('Card').children().at(1);
  const cardText = card.find('CardText').text();
  expect(cardText == 'Already have an account? Log in!')
});
