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

it('should have h1 tag', () => {
  expect(wrapper.find('h1')).toHaveLength(1);
  expect(wrapper.find('h1').text()).toBe('Taxi')
});
