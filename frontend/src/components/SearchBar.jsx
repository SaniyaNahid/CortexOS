function SearchBar() {
  return (
    <div className="search-container">

      <input
        type="text"
        placeholder="Search documents, projects or ask AI..."
      />

      <button>
        Search
      </button>

    </div>
  );
}

export default SearchBar;