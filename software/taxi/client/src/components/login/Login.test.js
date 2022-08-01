import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import Login from './Login';

Enzyme.configure({adapter: new Adapter()});

let wrapper;

beforeEach(() => {
    wrapper = shallow(<Login />);
  });

it('should render the Login component', () => {
    expect(wrapper).toBeTruthy();
  });

it('should contain Link components', () => {
  expect(wrapper.find('Link')).toHaveLength(2)
  expect(wrapper.find('Link').first().text()).toBe('Home')
});

it('should contain h1 tag', () => {
  expect(wrapper.find('h1')).toHaveLength(1)
  expect(wrapper.find('h1').text()).toBe('Log in')
});

it('should contain p tag', () => {
  expect(wrapper.find('p')).toHaveLength(1)
  expect(wrapper.find('p').text()).toEqual('Already have an account? Log in!')
});