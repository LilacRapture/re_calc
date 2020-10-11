latest_tag=$(git describe --abbrev=0 --tags)
version=${latest_tag#"v"}
ver_parts=( ${version//./ } )
((ver_parts[1]++))
new_version="v${ver_parts[0]}.${ver_parts[1]}"
git tag "$new_version"
echo "Created a new tag, $new_version"
git push --tags
