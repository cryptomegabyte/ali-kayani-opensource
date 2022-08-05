import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import Landing from './Landing';

Enzyme.configure({adapter: new Adapter()});

let wrapper;

beforeEach(() => {
    wrapper = shallow(<Landing />);
});

it('should render the Landing component', () => {
    expect(wrapper).toBeTruthy();
});

it('should contain a Button Group', () => {
  expect(wrapper.find('ButtonGroup')).toHaveLength(1)
});

it('should contain Link components', () => {
  expect(wrapper.find('LinkContainer')).toHaveLength(2)
});

it('should contain Button components', () => {
  expect(wrapper.find('Button')).toHaveLength(2)
  expect(wrapper.find('Button').at(0).text()).toBe('Sign up')
  expect(wrapper.find('Button').at(1).text()).toBe('Log in')
});


it('should contain h1 tag', () => {
  expect(wrapper.find('h1')).toHaveLength(1)
  expect(wrapper.find('h1').text()).toBe('Taxi')
});
