 import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import App from './App';

Enzyme.configure({adapter: new Adapter()});

let wrapper;

beforeEach(() => {
  wrapper = shallow(<App />);
});

it('should render the app', () => {
  expect(wrapper).toBeTruthy();
});

it('should contain a Routes component', () => {
  expect(wrapper.find('Routes')).toBeTruthy();
  expect(wrapper.find('Routes')).toHaveLength(1);
});

it('should contain a Route component', () => {
  expect(wrapper.find('Route')).toBeTruthy();
});

it('the Routes component should have three routes', () => {
  expect(wrapper.find('Route').children()).toHaveLength(3);
});
