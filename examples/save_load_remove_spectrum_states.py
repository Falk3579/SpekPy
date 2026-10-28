# For compatibility with Python2

import spekpy as sp

print("\n** Script to save, load and remove a new spectrum from disk **\n")

# Generate filtered spectrum
s=sp.Spek(kvp=120,th=12).filter('Al',2.5)
# Print summary of metrics
s.summarize(mode="full")
# Save spectrum as new state
state_name='My spectrum state'
s.save_state(state_name)
# See all user-saved states
sp.Spek.show_states(state_dir="usr")
# Load the new saved state
t=sp.Spek.load_state(state_name)
# Print summary of metrics (should be the same as above)
t.summarize(mode="full")
# Remove/delete te state
sp.Spek.remove_state('My spectrum state')
# See all user-saved states (new state should now have been removed)
sp.Spek.show_states(state_dir="usr")

