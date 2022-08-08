import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import Layout from './Layout';

Enzyme.configure({adapter: new Adapter()});

let wrapper;

beforeEach(() => {
    wrapper = shallow(<Layout isLoggedIn={true}/>);
  });

it('should render the SignUp component', () => {
  expect(wrapper).toBeTruthy();
});

it('should contain a Navbar component', () => {
    expect(wrapper.find('Navbar')).toBeTruthy();
  });
  
  it('that navbar component should have props', () => {
    expect(wrapper.find('Navbar').props().bg).toBe('light');
    expect(wrapper.find('Navbar').props().expand).toBe('lg');
    expect(wrapper.find('Navbar').props().variant).toBe('light');
  });
  
  it('should contain two container component', () => {
    expect(wrapper.find('Container')).toHaveLength(2);
  });
  
  it('should contain Link components', () => {
    expect(wrapper.find('LinkContainer')).toHaveLength(1)
  });
  
  it('that navbar component should have props', () => {
    expect(wrapper.find('Navbar').props().bg).toBe('light');
  });
  
  it('that navbar component should have props', () => {
    expect(wrapper.find('Navbar').props().bg).toBe('light');
    expect(wrapper.find('Navbar').props().expand).toBe('lg');
    expect(wrapper.find('Navbar').props().variant).toBe('light');
  });
  
  it('should contain an outlet component', () => {
    expect(wrapper.find('Outlet')).toBeTruthy();
  });
  
  it('should render the form and button component', () => {
    expect(wrapper.find('Form')).toBeTruthy();
    expect(wrapper.find('Button')).toBeTruthy();
    expect(wrapper.find('Button').text()).toBe('Log out');
  });

  it('should not render the form and button component', () => {
    const propsFalseWrapper = shallow(<Layout isLoggedIn={false} /> );
    expect(propsFalseWrapper.find('Form')).toHaveLength(0);
    expect(propsFalseWrapper.find('Button')).toHaveLength(0);
  });